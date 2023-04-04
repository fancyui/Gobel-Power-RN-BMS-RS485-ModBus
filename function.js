# caculate hex value for field length
# example: hex str info = "C2 06 C5 5C"

function fieldLength(info) {
    const dataArr = new Uint8Array(Buffer.from(info.replace(/\s/g, ''), 'hex'));
    const dataList = Array.from(dataArr);
    const lenid = dataList.length;
    const sumLenid = Math.floor(lenid / 16 / 16) + Math.floor(lenid / 16) + (lenid % 16);
    const modLenid = sumLenid % 16;
    const lchksum = 255 - modLenid + 1 - 240;
    const lchksumUp = lchksum * Math.pow(2, 12);
    const length = (lchksumUp + lenid).toString(16);

    return length;
}


#caculate hex value for field chksum
# hex str middle_data = VER + ADR + CID1 + CID2 + LENGTH + INFO
# example: middle_data = "11 01 46 C2 C0 04 C2 06 C5 5C"

function fieldChksum(middle_data) {
    const dataArr = new Uint8Array(Buffer.from(middle_data.replace(/\s/g, ''), 'hex'));
    const dataList = Array.from(dataArr);
    const sumDataList = dataList.reduce((acc, val) => acc + val, 0);
    const modSum = sumDataList % 65536;
    let chksum;

    if (modSum < 256) {
        chksum = 255 - modSum + 1;
    } else if (modSum < 65280) {
        chksum = 65279 - modSum + 1 + 256;
    } else {
        chksum = 255 - modSum + 1 + 65280;
    }

    return chksum.toString(16);
}

