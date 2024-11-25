# Typst Image to local package

This tool lets you install an image as a local typst package. Thus you do not need to include the image
in every project directory.

Usage:
```sh
$ python install.py <logo file> <package name>
```

This will create a package in your local package
directory.

On Windows:
`%AppData%/typst/packages/local/`

On Linux:
`~/.local/share/typst/packages/local/`

On MacOS:
`~/Library/Application Support/typst/packages/local/`