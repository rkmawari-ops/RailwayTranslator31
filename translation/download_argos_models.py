
import argostranslate.package

print("Updating package index...")

argostranslate.package.update_package_index()

packages = argostranslate.package.get_available_packages()

package_to_install = None

for package in packages:
    if package.from_code == "en" and package.to_code == "hi":
        package_to_install = package
        break

if package_to_install is None:
    print("English → Hindi package not found.")
    exit()

print("Downloading package...")

download_path = package_to_install.download()

print("Installing package...")

argostranslate.package.install_from_path(download_path)

print("Installation Complete!")