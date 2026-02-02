$rootDir = "c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"
$files = Get-ChildItem -Path $rootDir -Recurse -Filter "*.html"

foreach ($file in $files) {
    # Skip root index.html if it's the landing page (though usually we want to fix links IN it, but safety first)
    if ($file.Name -eq "index.html" -and $file.DirectoryName -eq $rootDir) {
        continue
    }

    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # 1. Navbar Home link (Root level)
    # <li><a href="index.html" class="active">Home</a></li> -> tokyo-in-film.html
    $content = $content -replace 'href="index\.html"([^>]*)>Home</a>', 'href="tokyo-in-film.html"$1>Home</a>'
    
    # 2. Navbar Home link (Subdirectory level)
    # <li><a href="../index.html">Home</a></li> -> ../tokyo-in-film.html
    $content = $content -replace 'href="\.\./index\.html"([^>]*)>Home</a>', 'href="../tokyo-in-film.html"$1>Home</a>'
    
    # 3. Footer/Body "Previous: Home" buttons
    # <a href="../index.html" class="btn">&larr; Previous: Home</a>
    $content = $content -replace 'href="\.\./index\.html"([^>]*)>\s*&larr; Previous: Home</a>', 'href="../tokyo-in-film.html"$1>&larr; Previous: Home</a>'
    $content = $content -replace 'href="\.\./index\.html"([^>]*)>\s*Previous: Home</a>', 'href="../tokyo-in-film.html"$1>Previous: Home</a>'

    if ($content -ne $originalContent) {
        Write-Host "Fixed: $($file.FullName)"
        $content | Set-Content -Path $file.FullName -Encoding UTF8
    }
}
