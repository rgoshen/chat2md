module.exports.readVersion = function (contents) {
    const match = contents.match(/version=['"]([^'"]+)['"]/)
    if (match && match[1]) {
        return match[1]
    }
    return false
}

module.exports.writeVersion = function (contents, version) {
    return contents.replace(/version=['"][^'"]+['"]/, `version='${version}'`)
}