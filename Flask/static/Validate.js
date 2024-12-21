document.addEventListener('DOMContentLoaded', function () {
        const form = document.querySelector('form');

        form.addEventListener('submit', function (event) {
                let valid = true;

                const firstName = form.elements['first_name'].value;
                if (!/^[a-zA-Z]+$/.test(firstName)) {
                        alert('Enter a valid first name (only letters).');
                        valid = false;
                }

                const lastName = form.elements['last_name'].value;
                if (!/^[a-zA-Z]+$/.test(lastName)) {
                        alert('Enter a valid last name (only letters).');
                        valid = false;
                }

                const email = form.elements['email'].value;
                const emailPattern = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
                if (!emailPattern.test(email)) {
                        alert('Enter a valid email (example@example.example).');
                        valid = false;
                }

                const password = form.elements['password'].value;
                const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$/;
                if (!passwordPattern.test(password)) {
                        alert('Enter a valid password (at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character).');
                        valid = false;
                }

                if (!valid) {
                        event.preventDefault();
                }
        });
});