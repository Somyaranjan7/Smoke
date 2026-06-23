window.onload = function() {

    setTimeout(

        function() {

            let flashMessages =
                document.getElementsByClassName(
                    "flash-message"
                );

            for (

                let i = 0;

                i < flashMessages.length;

                i++

            ) {

                flashMessages[i].style.display =
                    "none";

            }

        },

        3000

    );

};