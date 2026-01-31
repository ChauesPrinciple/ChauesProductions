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
            $content = $content.Replace("'€™", "'")
            $content = $content.Replace("'€˜", "'")
            $content = $content.Replace("'€“", " – ")
            $content = $content.Replace("'€”", " — ")
            $content = $content.Replace("'€œ", '"')
            $content = $content.Replace("'€", '"')

            # Special Japanese/French artifacts
            $content = $content.Replace("è¨ne", "ène")
            $content = $content.Replace("è©ne", "ène") 
            
            # Méliès -> Mè©liè¨s
            $content = $content.Replace("è©", "é")
            $content = $content.Replace("è¨s", "ès")

            # Ōtomo -> è”tomo (using hex unicode for safety if needed, but trying literal first)
            $content = $content.Replace("è”tomo", "Ōtomo")
            
            # Kōhei -> è»hei
            $content = $content.Replace("è»hei", "Kōhei")

            # Generic cleanups
            $content = $content.Replace("'˜", "'")
            $content = $content.Replace("'€¦", "…")


            if ($content -ne $originalContent) {
                [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
                Write-Host "Fixed: $($file.Name)"
            }
        }
    }
}
Write-Host "Encoding fix complete."
