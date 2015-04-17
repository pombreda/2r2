Pour downloader:

    cd static/
    wget -e robots=off -H -p -k http://2r2.ca/
    wget -e robots=off -H -p -k http://2r2.ca/thermographie/
    wget -e robots=off -H -p -k http://2r2.ca/thermographie/nouvelles/
    wget -e robots=off -H -p -k http://2r2.ca/thermographie/services/
    wget -e robots=off -H -p -k http://2r2.ca/thermographie/coordonnees/
    wget -e robots=off -H -p -k http://2r2.ca/thermographie/hello-world/
    wget -e robots=off -H -p -k http://2r2.ca/thermography/
    wget -e robots=off -H -p -k http://2r2.ca/thermography/news/
    wget -e robots=off -H -p -k http://2r2.ca/thermography/services/
    wget -e robots=off -H -p -k http://2r2.ca/thermography/sample-page/
    cd ..
    python fix.py
    git commit -a -m "First pass"
    git sed 's#http://2r2.ca##'
    git sed 's#/thermographie"#/thermographie/index.html"#'
    git sed 's#/thermographie/"#/thermographie/index.html"#'
    git sed 's#/thermography"#/thermography/index.html"#'
    git sed 's#/thermography/"#/thermography/index.html"#'
    git sed 's#/nouvelles/"#/nouvelles/index.html"#'
    git sed 's#/hello-world/"#/hello-world/index.html"#'
    git sed 's#/services/"#/services/index.html"#'
    git sed 's#/coordonnees/"#/coordonnees/index.html"#'
    git sed 's#/news/"#/news/index.html"#'
    git sed 's#/sample-page/"#/sample-page/index.html"#'

