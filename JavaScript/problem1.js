let data = [
    "   + -- + - + -   ",
    "   + --- + - +   ",
    "   + -- + - + -   ",
    "   + - + - + - +   "
];

let t = "";

for (var s of data) {
    t += String.fromCharCode(
        parseInt(
            Number(s.replace(/ /g, "").replace(/\+/g, "1").replace(/-/g, "0")),
            2
        )
    );
}

console.log(t);