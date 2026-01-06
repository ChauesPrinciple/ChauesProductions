
$root = "c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"
$target = '<div class="logo">Tokyo in Film</div>'
$replacement = @"
<div class="logo">
    Tokyo in Film
    <div class="dropdown-menu">
        <a href="https://chauesprinciple.github.io/Tokyo-in-Film/" class="dropdown-item current">Tokyo in Film</a>
        <a href="https://chauesprinciple.github.io/Ancient-literature/" class="dropdown-item">Ancient Literature</a>
    </div>
</div>
"@

Get-ChildItem -Path $root -Filter *.html -Recurse | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    if ($content.Contains($target)) {
        $content = $content.Replace($target, $replacement)
        Set-Content -Path $_.FullName -Value $content -Encoding UTF8
        Write-Host "Updated $($_.Name)"
    }
}
