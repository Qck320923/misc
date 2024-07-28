//仅作为对Array模块的补充，也可以把这些函数存为Array的方法。
//Just as a supplement to the Array module, you can also save these functions as the Array methods.
/**
 * @description 重复数组
 * @param {any[]} list 数组
 * @param {number} count 次数
 * @returns {any[]}
 */
repeat(list, count) {
    if (!list.length || count <= 0) return [];
    let res = [];
    for (let i = 1; i < count; i++) {
        res = res.concat(list);
    }
    return res;
}
