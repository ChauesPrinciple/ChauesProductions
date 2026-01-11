$baseUrl = "https://chaues.carrd.co"

# Define assets to download (URL suffix -> Local path)
# Note: The HTML references images with query strings ?v=...
# We will download them to the clean filenames expected by the HTML (ignoring the query string in the filename on disk, 
# but we need to match what the browser will request if we don't change the HTML? 
# The HTML has src="assets/images/bg.jpg?v=d5a9c4ba". Local file server usually ignores query strings for static files, 
# or we need to ensure the file exists as bg.jpg. Browser resolves to bg.jpg logic usually.
# Actually, if I open `landing.html` locally, `assets/images/bg.jpg?v=...` might fail if the file system is strict? 
# Browsers on file:// protocol might treat ?v=... as part of the filename? 
# Usually 'file://.../bg.jpg?v=...' fails. 
# BUT the user HTML has these query strings. I should probably STRIP them from the HTML or save files WITH the query string? 
# Windows filenames can't contain '?'. 
# So I MUST modify the HTML to remove `?v=...`. 
# I will download to clean filenames and later (or during write) clean the HTML.

$downloads = @{
    "assets/images/bg.jpg"                          = "assets/images/bg.jpg?v=d5a9c4ba"
    "assets/images/image07.png"                     = "assets/images/image07.png?v=d5a9c4ba"
    "assets/images/image01.png"                     = "assets/images/image01.png?v=d5a9c4ba"
    "assets/images/image02.png"                     = "assets/images/image02.png?v=d5a9c4ba"
    "assets/images/gallery01/26e244bf.jpg"          = "assets/images/gallery01/26e244bf.jpg?v=d5a9c4ba"
    "assets/images/gallery01/26e244bf_original.jpg" = "assets/images/gallery01/26e244bf_original.jpg?v=d5a9c4ba"
    "assets/images/gallery01/d3df87c0.jpg"          = "assets/images/gallery01/d3df87c0.jpg?v=d5a9c4ba"
    "assets/images/gallery01/d3df87c0_original.jpg" = "assets/images/gallery01/d3df87c0_original.jpg?v=d5a9c4ba"
    "assets/images/gallery01/be369aa0.jpg"          = "assets/images/gallery01/be369aa0.jpg?v=d5a9c4ba"
    "assets/images/gallery01/be369aa0_original.jpg" = "assets/images/gallery01/be369aa0_original.jpg?v=d5a9c4ba"
}

# Create directories
New-Item -ItemType Directory -Force -Path "assets/images"
New-Item -ItemType Directory -Force -Path "assets/images/gallery01"

foreach ($key in $downloads.Keys) {
    $url = "$baseUrl/$($downloads[$key])"
    $output = $key
    Write-Host "Downloading $url to $output"
    try {
        Invoke-WebRequest -Uri $url -OutFile $output
    }
    catch {
        Write-Error "Failed to download $url"
    }
}
