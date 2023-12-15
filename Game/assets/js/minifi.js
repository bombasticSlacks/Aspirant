function clearHeaderAnchor(node) {}

window.addEventListener(
  "message",
  (e) => {
    if (e.data === "minify") {
      const anchorVal = window.location.hash;
      if (anchorVal !== "") {
        var adding = false;
        var hType;
        var nodeList = [];
        for (const child of document.querySelector("main").childNodes) {

          if (adding) {
            if (
              child.nodeName === "H1" ||
              child.nodeName === "H2" ||
              child.nodeName === "H3" ||
              child.nodeName === "H4" ||
              child.nodeName === "H5" ||
              child.nodeName === "H6"
            ) {
              if (Number(child.nodeName.charAt(1)) <= Number(hType)) {
                adding = false;
                break;
              }
            }
            nodeList.push(child);
          } else if (child.id === anchorVal.substring(1)) {
            adding = true;
            nodeList.push(child);
            hType = child.nodeName.charAt(1);
          }
        }
        const node = document.querySelector("main");
        node.innerHTML = "";
        for (const child of nodeList) {
          node.appendChild(child);
        }
      }

      const main = document.querySelector(".main-content-wrap");
      document.body.innerHTML = "";
      document.body.appendChild(main);

      document.querySelector("footer").innerHTML = "";

      // Tell the parent that we are done modifying the DOM
      window.parent.postMessage("done", "*");
    }
  },
  false
);
