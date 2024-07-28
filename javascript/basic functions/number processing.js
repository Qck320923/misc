//仅作为对Math模块的补充，也可以把这些函数存为Math模块的方法。
//Just as a supplement to the Math module, you can also save these functions as the Math module methods.
/**
 * @description 随机小数
 * @param {number} low 最低值
 * @param {number} high 最高值
 * @param {number} size 相邻可能返回值之间的间隔
 * @example randfloat(0, 1)的返回值在0到1之间(0≤returnValue≤1)
 * @example randfloat(0, 1, 0.1)的返回值在[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]之中
 * @example randfloat(0, 0.1, 0.2)的返回值为0
 * @example randfloat(0, 10, 1)的返回值在[0,1,2,3,4,5,6,7,8,9,10]之中
 * @returns {number} 随机结果
 */
function randfloat(low, high, size = null) {
    if (size) return this.floor(low + Math.round(Math.random() * Math.floor((high - low) / size)) * size, this.fractionalPartLength(size));
    else return this.floor(low + Math.random() * (high - low));
}
/**
 * @description 随机整数
 * @param {number} low 最低值
 * @param {number} high 最高值
 * @param {number} size 相邻可能返回值之间的间隔（最小为1）
 * @example randint(0, 100)的返回值在0到100之间(0≤returnValue≤1)
 * @example randint(0, 100, 20)的返回值在[0,20,40,60,80,100]之中
 * @example randint(0, 10, 0.1)的返回值在[0,1,2,3,4,5,6,7,8,9,10]之中
 * @example randint(0, 100, 200)的返回值为0
 * @returns {number} 随机结果
 */
function randint(low, high, size = null) {
    if (size) return Math.round(low + Math.floor(Math.random() * (high - low) / size) * size);
    else return Math.round(low + Math.random() * (high - low));
}
/**
 * @description 四舍五入
 * @param {number} x 数
 * @param {number} n 要保留的位数，默认为0
 * @returns {number} 四舍五入后的数
 */
function round(x, n) {
    return Math.round(x * Math.pow(10, n)) / Math.pow(10, n);
}
/**
 * @description 向下取整
 * @param {number} x 数
 * @param {number} n 要保留的位数，默认为0
 * @returns {number} 向下取整后的数
 */
function floor(x, n) {
    return Math.floor(x * Math.pow(10, n)) / Math.pow(10, n);
}
/**
 * @description 向上取整
 * @param {number} x 数
 * @param {number} n 要保留的位数，默认为0
 * @returns {number} 向上取整后的数
 */
function ceil(x, n = 0) {
    return Math.ceil(x * Math.pow(10, n)) / Math.pow(10, n);
}
/**
 * @description 小数部分长度
 * @param {number} x 数
 * @returns {number} 返回小数部分的长度
 */
function fractionalPartLength(x) {
    let parts = String(x).split(".");
    if (!parts[1]) return 0;
    return parts[1].length;
}
/**
 * @description 取总和
 * @param {number[]} x 数
 * @returns {number} 总和
 */
function sum(...x) {
    return x.reduce(function (sum, val) { return sum + val }, 0);
}
/**
 * @description 取平均数
 * @param {number[]} x 数
 * @returns {number} 平均数
 */
function average(...x) {
    return x.reduce(function (sum, val) { return sum + val }, 0) / x.length;
}
