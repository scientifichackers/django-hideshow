(function () {
    Set.prototype.diff = function (other) {
        let ret = new Set(this);
        for (let elem of other) {
            ret.delete(elem);
        }
        return ret;
    };

    document.addEventListener("DOMContentLoaded", function () {
        let nodes = document.querySelectorAll("[--hideshow-fields]");

        for (let node of nodes) {
            let onChange;

            let hideFields = new Set(csvParse(node.getAttribute("--hideshow-fields")));

            switch (node.type) {
                case "select-one":
                    onChange = function () {
                        let value = node.value;

                        let showOnSelected;
                        if (value) {
                            showOnSelected = csvParse(
                                node.getAttribute(`--show-on-${value}`)
                            );
                        }

                        let toShow = showOnSelected || [];
                        let toHide = hideFields.diff(toShow);

                        getFormRows(toShow).map(show);
                        getFormRows(toHide).map(hide);
                    };

                    break;

                case "checkbox":
                    let showOnChecked = csvParse(node.getAttribute("--show-on-checked"));

                    let toShow = showOnChecked || [];
                    let toHide = hideFields.diff(toShow);

                    let showRows = getFormRows(toShow);
                    let hideRows = getFormRows(toHide);

                    onChange = function () {
                        let checked = node.checked;
                        hideRows.map(checked ? hide : show);
                        showRows.map(checked ? show : hide);
                    };

                    break;
            }

            if (onChange) {
                onChange();
                node.addEventListener("change", onChange);
            }
        }
    });

    function csvParse(str) {
        if (!str) {
            return [];
        }
        let arr = str.split(",");
        for (let i = 0; i < arr.length; i++) {
            arr[i] = arr[i].trim();
        }
        return arr;
    }

    function getFormRows(fields) {
        return Array.from(_getFormRows(fields));
    }

    function* _getFormRows(fields) {
        if (!fields) {
            return;
        }
        for (let name of fields) {
            let formRow = fieldNameToFormRow(name);
            if (!formRow) continue;
            yield formRow;
        }
    }

    function fieldNameToFormRow(fieldName) {
        let cls = "field-" + fieldName;
        let formRow = document.getElementsByClassName(cls)[0];
        return formRow;
    }

    function hide(node) {
        node.style.display = "none";
    }

    function show(node) {
        node.style.display = "";
    }
})();