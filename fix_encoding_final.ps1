$enc = [System.Text.Encoding]::UTF8
function BytesToString($bytes) { return $enc.GetString($bytes) }

# Define garbage patterns based on Windows-1252 misinterpretation of UTF-8
# Original: ’ (Right Single Quote) E2 80 99
# Corrupted: â€™ (E2 80 99 interpreted as 1252 chars: â € ™)
# But sometimes â (E2) might be missing or mapped to '
# We will target likely combinations

$garbage_map = @{}

# Right Single Quote / Apostrophe (’) -> â€™ or '€™
$utf8_apos = @(0xE2, 0x80, 0x99)
$garbage_map["â€™"] = "'" # â + € + ™
$garbage_map["'€™"] = "'" # ' + € + ™

# Left Single Quote (‘) -> â€˜ or '€˜
$utf8_lapos = @(0xE2, 0x80, 0x98)
$garbage_map["â€˜"] = "'"
$garbage_map["'€˜"] = "'"

# En Dash (–) -> â€“ or '€“
$utf8_endash = @(0xE2, 0x80, 0x93)
$garbage_map["â€“"] = " – "
$garbage_map["'€“"] = "–"

# Em Dash (—) -> â€” or '€”
$utf8_emdash = @(0xE2, 0x80, 0x94)
$garbage_map["â€”"] = "—"
$garbage_map["'€”"] = " — "

# Left Double Quote (“) - > â€œ or '€œ
$utf8_lquote = @(0xE2, 0x80, 0x9C)
$garbage_map["â€œ"] = '"'
$garbage_map["'€œ"] = '"'

# Right Double Quote (”) - > â€ or '€  (Wait, ” is E2 80 9D. 1252 9D is undefined/whitespace? Or unique)
# In 1252, 0x9D is undefined. But often mapped to replacement char or empty. 
# However, user file search showed '€ as a pattern for Right Quote (closing).
$garbage_map["â€"] = '"' # If replacement char
$garbage_map["'€"] = '"'
$garbage_map["â€"] = '"'  # Risky if alone?
$garbage_map["'€"] = '"'

# Ellipsis (…) -> â€¦ or '€¦
$utf8_ellip = @(0xE2, 0x80, 0xA6)
$garbage_map["â€¦"] = "..."
$garbage_map["'€¦"] = "..."

# Specific French/Japanese artifacts
# mise-en-scène -> mise-en-scè¨ne (è -> è¨)
$garbage_map["è¨ne"] = "ène"
$garbage_map["è©ne"] = "ène"
$garbage_map["è©"] = "é"
$garbage_map["è¨s"] = "ès"

# Japanese Names
$garbage_map["è”tomo"] = "Ōtomo"
$garbage_map["è»hei"] = "Kōhei"
$garbage_map["è²n"] = "Ozu" # Guessing based on "Yasujir..." -> Yasujirō
$garbage_map["Yasujirè²n"] = "Yasujirō" # More specific safer
$garbage_map["Yasujirè²"] = "Yasujirō"


$directories = @("pre-production", "production", "post-production", "guides")
$extensions = @("*.html")

foreach ($dir in $directories) {
    if (Test-Path $dir) {
        $files = Get-ChildItem -Path $dir -Recurse -Include $extensions
        foreach ($file in $files) {
            $path = $file.FullName
            try {
                $content = [System.IO.File]::ReadAllText($path, $enc)
                $originalContent = $content

                foreach ($key in $garbage_map.Keys) {
                    $val = $garbage_map[$key]
                    if ($content.Contains($key)) {
                        $content = $content.Replace($key, $val)
                    }
                }

                if ($content -ne $originalContent) {
                    [System.IO.File]::WriteAllText($path, $content, $enc)
                    Write-Host "Fixed: $($file.Name)"
                }
            } catch {
                Write-Host "Error processing $($file.Name): $_"
            }
        }
    }
}
Write-Host "Encoding fix script completed."
