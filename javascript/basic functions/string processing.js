//仅作为对String类方法的补充，也可以把这些函数存为String类的方法。
//Just as a supplement to the String class method, you can also save these functions as methods of the String class.
/*
/**
 * @description 统计字符串中出现某字符串的次数
 * @param {string} otherStr 另一个字符串
 * @param {number} start 开始下标
 * @param {number} end 结束下标
 * @returns {number}
 */
String.prototype.count = function (otherStr, start = 0, end = -1) {
    var cnt = 0;
    for (var i = start; i <= ((end >= 0) ? end : (this.length + end)) - otherStr.length + 1; i++) {
        if (this.slice(i, i + otherStr.length) === otherStr) cnt++;
    }
    return cnt;
}
*/
/**
 * @description 统计字符串中出现某字符串的次数
 * @param {string} str1 字符串1
 * @param {string} str2 字符串2
 * @param {number} start 开始下标
 * @param {number} end 结束下标
 * @returns {number}
 */
function count(str1, str2, start = 0, end = -1) {
    var cnt = 0;
    for (var i = start; i <= ((end >= 0) ? (end) : (str1.length + end)) - str2.length + 1; i++) {
        if (str1.slice(i, i + str2.length) === str2) cnt++;
    }
    return cnt;
}
