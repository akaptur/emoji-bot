letters = "abcdefghijklmnopqrstuvwxyz"
emo = {}

function store_emoji (keys){
    $(".new_message_textarea").val(":"+keys)
    $(".new_message_textarea").keyup()

    var emojis = $(".typeahead.dropdown-menu")[3].children

    for (var i = 0; i < emojis.length; i++ ) {
        name = emojis[i].children[0].children[0].src.slice(51,-4)
        if (!emo[name]) {
            emo[name] = true
        }
    }

}

var time = 0
for (i = 0; i < letters.length; i++) {
    for (j = 0; j < letters.length; j++) {
        for (k = 0; k < letters.length; k++) {
            time += 100;
            keys = letters[i]+letters[j]+letters[k];
            (function (keys) {
                setTimeout(function() {
                    store_emoji(keys)
                }, time)
            })(keys)
        }
    }
}

Object.keys(emo).forEach (function (key) {console.log(key)})
