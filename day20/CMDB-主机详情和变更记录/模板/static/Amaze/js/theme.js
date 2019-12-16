var saveSelectColor = {'Name': 'SelcetColor', 'Color': 'theme-black'}
if (storageLoad('SelcetColor')) {
    $('body').attr('class', storageLoad('SelcetColor').Color)
} else {
    storageSave(saveSelectColor);
    $('body').attr('class', 'theme-black')
}

function storageSave(objectData) {
    localStorage.setItem(objectData.Name, JSON.stringify(objectData));
}

function storageLoad(objectName) {
    if (localStorage.getItem(objectName)) {
        return JSON.parse(localStorage.getItem(objectName))
    } else {
        return false
    }
}