/*参考：https://blog.csdn.net/crr411422/article/details/131149849*/
class Node {
    constructor(symbol, frequency, left = null, right = null) {
        this.symbol = symbol;
        this.frequency = frequency;
        this.left = left;
        this.right = right;
    }
}

function swapNodes(arr, i, j) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

function heapify(arr, n, i) {
    var smallest = i;
    var left = 2 * i + 1;
    var right = 2 * i + 2;
    if (left < n && arr[left].frequency < arr[smallest].frequency) smallest = left;
    if (right < n && arr[right].frequency < arr[smallest].frequency) smallest = right;
    if (smallest !== i) {
        swapNodes(arr, i, smallest);
        heapify(arr, n, smallest);
    }
}

function buildMinHeap(arr, n) {
    for (var i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

function extractMin(arr, n) {
    var minNode = arr[0];
    arr[0] = arr[n - 1];
    n--;
    heapify(arr, n, 0);
    return minNode;
}

function insertMinHeap(arr, n, newNode) {
    n++;
    var i = n - 1;
    while (i > 0 && newNode.frequency < arr[Math.floor((i - 1) / 2)].frequency) {
        arr[i] = arr[Math.floor((i - 1) / 2)];
        i = Math.floor((i - 1) / 2);
    }
    arr[i] = newNode;
}

function generateCodes(root, codes = [], top = 0) {
    var res = {};
    if (root.left) {
        codes.push(0);
        Object.assign(res, generateCodes(root.left, codes, top + 1));
        codes.pop();
    }
    if (root.right) {
        codes.push(1);
        Object.assign(res, generateCodes(root.right, codes, top + 1));
        codes.pop();
    }
    if (!root.left && !root.right) {
        res[root.symbol] = codes.slice(0, top).join("");
    }
    return res;
}

function encode(clear) {
    if (!clear.length) return { root: null, code: "" };
    var frequency = {};
    for (var char of clear) frequency[char] = (frequency[char] || 0) + 1;
    var n = 0;
    var minHeap = [];
    for (var symbol in frequency) {
        if (frequency.hasOwnProperty(symbol)) {
            minHeap.push(new Node(symbol.charCodeAt(0), frequency[symbol]));
            n++;
        }
    }
    var heapSize = n;
    buildMinHeap(minHeap, heapSize);
    while (heapSize > 1) {
        var left = extractMin(minHeap, heapSize);
        heapSize--;
        var right = extractMin(minHeap, heapSize);
        heapSize--;
        var newNode = new Node(-1, left.frequency + right.frequency);
        newNode.left = left;
        newNode.right = right;
        insertMinHeap(minHeap, heapSize, newNode);
        heapSize++;
    }
    var codesMap = generateCodes(minHeap[0], [], 0);
    var code = "";
    for (var i = 0; i < clear.length; i++) code = code.concat(String(codesMap[clear.charCodeAt(i)]));
    return { root: minHeap[0], code };
}

function decode(root, cipher) {
    if (!(root && cipher.length)) return "";
    var clear = "";
    var currentNode = root;
    for (var i = 0; i < cipher.length;) {
        if (cipher[i] === "0") {
            if (currentNode.left) {
                currentNode = currentNode.left;
                i++;
            } else {
                clear += String.fromCharCode(currentNode.symbol);
                currentNode = root;
            }
        } else if (cipher[i] === "1") {
            if (currentNode.right) {
                currentNode = currentNode.right;
                i++;
            } else {
                clear += String.fromCharCode(currentNode.symbol);
                currentNode = root;
            }
        }
        if (!currentNode.left && !currentNode.right) {
            clear += String.fromCharCode(currentNode.symbol);
            currentNode = root;
        }
    }
    return clear;
}
