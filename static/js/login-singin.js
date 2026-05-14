const password_entry = document.getElementById("password");
const alert = document.getElementById("password-sec");

password_entry.addEventListener("input", () => {
    if (password_entry.value != "")
    {
        console.log(toString(password_entry.value).length)
        if (toString(password_entry.value).length >= 8) 
        {
            alert.textContent = "Segura";
        }
        else
        {
            alert.textContent = "Insegura";
        }

    }
    else
    {
        return
    }
});