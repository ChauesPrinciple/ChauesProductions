$content = [System.IO.File]::ReadAllText("guides/local-business-commercial-guide.html", [System.Text.Encoding]::UTF8)
$index = $content.IndexOf("€")
if ($index -ge 0) {
    if ($index + 10 -gt $content.Length) { $length = $content.Length - $index } else { $length = 10 }
    $substring = $content.Substring($index, $length)
    Write-Host "Found pattern at index ${index}: '$substring'"
    Write-Host "Char codes:"
    foreach ($c in $substring.ToCharArray()) {
        Write-Host ([int]$c)
    }
}
else {
    Write-Host "Pattern not found."
}
