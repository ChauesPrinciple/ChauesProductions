$files = @(
    "guides/action-units-worksheet.html",
    "guides/fight-scene-structure-worksheet.html",
    "guides/local-business-commercial-guide.html",
    "guides/location-exploration-guide.html",
    "guides/motivated-camera-movement.html",
    "guides/TOKYO THREE-SHOT WORKSHEET.html"
)

foreach ($file in $files) {
    Write-Host "Fixing $file..."
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # Fix all encoding errors
    $content = $content -replace 'è¢'‚¬'„¢', "'"
    $content = $content -replace 'è¢'‚¬'€œ', '—'
    $content = $content -replace 'è¢'‚¬'€', '—'
    $content = $content -replace 'è¢'‚¬Å"', '"'
    $content = $content -replace 'è¢'‚¬ï¿½', '"'
    $content = $content -replace 'è¢'‚¬', "'"
    
    # Write back
    Set-Content $file -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Fixed $file"
}

Write-Host "All files fixed!"
