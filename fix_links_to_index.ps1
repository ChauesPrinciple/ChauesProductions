$rootDir = "c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"
$files = Get-ChildItem -Path $rootDir -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Target: href="tokyo-in-film.html" -> href="index.html"
    # Target: href="../tokyo-in-film.html" -> href="../index.html"
    
    # 1. Root level replacements
    $content = $content -replace 'href="tokyo-in-film.html"', 'href="index.html"'
    
    # 2. Subdirectory level replacements
    $content = $content -replace 'href="\.\./tokyo-in-film.html"', 'href="../index.html"'
    
    # 3. Fix the Dropdown link explicitly to be absolute or root relative if needed? 
    # The user liked the pre-production bar. It had: <a href="https://chauesprinciple.github.io/Tokyo-in-Film/" ...>
    # My tokyo-in-film.html had: <a href="tokyo-in-film.html" ...>
    # Let's standardize the "Tokyo in Film" dropdown item to point to the absolute URL or root index.
    
    # Replace the dropdown item specific line if it matches the relative link
    $content = $content -replace '<a href="index.html" class="dropdown-item current">Tokyo in', '<a href="https://chauesprinciple.github.io/Tokyo-in-Film/" class="dropdown-item current">Tokyo in'

    if ($content -ne $originalContent) {
        Write-Host "Fixed: $($file.FullName)"
        $content | Set-Content -Path $file.FullName -Encoding UTF8
    }
}
