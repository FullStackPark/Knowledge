## Option 1: Command-line download extension as zip and extract

```sh
extension_id=jifpbeccnghkjeaalbbjmodiffmgedin   # change this ID
curl -L -o "$extension_id.zip" "https://clients2.google.com/service/update2/crx?response=redirect&os=mac&arch=x86-64&nacl_arch=x86-64&prod=chromecrx&prodchannel=stable&prodversion=44.0.2403.130&x=id%3D$extension_id%26uc" 
unzip -d "$extension_id-source" "$extension_id.zip"
```

Thx to crxviewer for the [magic download URL](https://github.com/Rob--W/crxviewer/blob/6113c25e3569e1ec59365ad9a177aa97e2bcda61/src/cws_pattern.js#L27-L74). 

## Option 2: Use the CRX Viewer extension 

The [Chrome extension source viewer](https://chrome.google.com/webstore/detail/chrome-extension-source-v/jifpbeccnghkjeaalbbjmodiffmgedin?hl=en) is open source ([github repo](https://github.com/Rob--W/crxviewer)) and makes this super easy.

![7170369c-cd61-411a-8bf3-a0b07d35be91](https://user-images.githubusercontent.com/32263380/39686748-7a05153c-51fd-11e8-946f-d32d7c64b803.png)

## Option 3: View source of locally installed extension

1. Find your Chrome local profile directory. Open `chrome://version/` and find the "Profile Path:` field. Open that folder up.
2. Open the `Extensions/` subfolder
3. All your extensions are here, with typically readable source. 

### Mapping between locally installed extension IDs and names
* On `about:extensions`, turn on Developer Mode and you'll see IDs under each entry
* Inside the `Extensions/` folders, the manifest.json has a readable `name` field

![image](https://cloud.githubusercontent.com/assets/39191/9500889/d7ffe65a-4bdc-11e5-9cfd-06ac0cbe5497.png)

