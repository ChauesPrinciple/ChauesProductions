$enc = [System.Text.Encoding]::UTF8

# Construct patterns using char codes to avoid script encoding issues
# ' = 39
# € = 8364
# ™ = 8482
# – = 8211
# — = 8212
# œ = 339
# è = 232
# ¨ = 168
# © = 169
# ” = 8221
# » = 187
# ² = 178

$garbage_map = @{}

# '€™ -> '
$k1 = [char]39 + [char]8364 + [char]8482
$garbage_map[$k1] = "'"

# '€˜ -> '
# ‘ = 8216
# '€˜ ... ˜ = 732 ? No, ‘ is Left Quote.
# Wait, pattern was '€˜. ˜ is tilde 732?
# Let's assume matches meant Left Quote.
$k_lq = [char]39 + [char]8364 + [char]732 
# Wait, small tilde is 732. If it was left quote...
# Pattern '€˜ might correspond to ’?? No.
# I will skip '€˜ unless verified.
# BUT '€ is handled below.

# '€“ -> –
$k2 = [char]39 + [char]8364 + [char]8211
$garbage_map[$k2] = "–"

# '€” -> —
$k3 = [char]39 + [char]8364 + [char]8212
$garbage_map[$k3] = "—"

# '€œ -> "
$k4 = [char]39 + [char]8364 + [char]339
$garbage_map[$k4] = '"'

# '€ -> " (Right quote or generic)
$k5 = [char]39 + [char]8364
$garbage_map[$k5] = '"'


# mise-en-scène path
# è¨ne -> ène
$k_mise = [char]232 + [char]168 + "ne"
$garbage_map[$k_mise] = "ène"

# è©ne -> ène
$k_mise2 = [char]232 + [char]169 + "ne"
$garbage_map[$k_mise2] = "ène"

# è© -> é  (232 169 -> 233)
$k_e = [char]232 + [char]169
$garbage_map[$k_e] = "é"


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

                # Apply replacements - Keys are NOT sorted order in hashtable, so we iterate array of keys
                # We need specific order
                $keys = $garbage_map.Keys | Sort-Object -Property Length -Descending
                
                foreach ($key in $keys) {
                    $val = $garbage_map[$key]
                    if ($content.Contains($key)) {
                        $content = $content.Replace($key, $val)
                    }
                }
                
                # Special fallback for '€ alone if map order missed it? 
                # (Sorted descending length handles '€ last correctly)

                if ($content -ne $originalContent) {
                    [System.IO.File]::WriteAllText($path, $content, $enc)
                    Write-Host "Fixed: $($file.Name)"
                }
            }
            catch {
                Write-Host "Error processing $($file.Name): $_"
            }
        }
    }
}
Write-Host "Safe fix script completed."
