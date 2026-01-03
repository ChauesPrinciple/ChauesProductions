$directories = @("pre-production", "production", "post-production", "guides")
$extensions = @("*.html")

foreach ($dir in $directories) {
    if (Test-Path $dir) {
        $files = Get-ChildItem -Path $dir -Recurse -Include $extensions
        foreach ($file in $files) {
            $path = $file.FullName
            $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
            
            $originalContent = $content

            # Order matters: match longer sequences first
            # '€™ -> '
            $content = $content.Replace("'€™", "'")
            # '€˜ -> '
            $content = $content.Replace("'€˜", "'")
            # '€“ -> – (en dash)
            $content = $content.Replace("'€“", " – ")
            # '€” - > — (em dash)
                $content = $content.Replace("'€”", " — ")
            # '€œ -> " (left double quote)
                    $content = $content.Replace("'€œ", '"')
            
                    # '€ -> " (right double quote - often appears as closing quote)
                    # CAUTION: '€ is also prefix of above. Check above replacements happened first.
                    # But wait, Replace() does not re-process replaced text.
                    # However, if '€ appears alone (e.g. at end of word” -> '€), it should be replaced.
                    # But what if '€ is part of valid text? Unlikely in this context.
                    $content = $content.Replace("'€", '"')

                    # Special Japanese/French artifacts
                    # mise-en-scène path
                    $content = $content.Replace("è¨ne", "ène")
                    $content = $content.Replace("è©ne", "ène") # saw this in list too?
            
                    # Méliès -> Mè©liè¨s
                    $content = $content.Replace("è©", "é")
                    $content = $content.Replace("è¨s", "ès")

                    # Ōtomo -> è”tomo
                    $content = $content.Replace("è”tomo", "Ōtomo")
            
            # Kōhei -> è»hei
            $content = $content.Replace("è»hei", "Kōhei")

            # Yasujirō -> è²n ?? Not sure on valid, but let's check common failures
            # If we don't fix it perfectly, at least fix the Quotes which are 99%.

            # Also '˜ which was in the list? '˜ -> ˜ (tilde?) OR '˜ -> '
            # List had '˜. Probably just noise or apostrophe.
            $content = $content.Replace("'˜", "'")

            # '€¦ -> … (ellipsis)
            $content = $content.Replace("'€¦", "…")


            if ($content -ne $originalContent) {
                [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
                Write-Host "Fixed: $($file.Name)"
            }
        }
    }
}
Write-Host "Encoding fix complete."
