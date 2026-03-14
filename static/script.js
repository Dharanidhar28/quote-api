const API_URL = "http://127.0.0.1:5000/quotes"

function loadQuotes() {

    fetch(API_URL)
    .then(response => response.json())
    .then(data => {

        const list = document.getElementById("quoteList")
        list.innerHTML = ""

        data.forEach(q => {

            const li = document.createElement("li")

            li.innerHTML = `
                ${q.quote}

                <button onclick="editQuote(${q.id}, '${q.quote}')">Edit</button>
                <button onclick="deleteQuote(${q.id})">Delete</button>
            `

            list.appendChild(li)

        })
    })
}


function addQuote() {

    const quoteText = document.getElementById("quoteInput").value

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            quote: quoteText
        })
    })
    .then(() => {
        document.getElementById("quoteInput").value = ""
        loadQuotes()
    })

}


function deleteQuote(id) {

    fetch(API_URL + "/" + id, {
        method: "DELETE"
    })
    .then(() => loadQuotes())

}


function editQuote(id, oldQuote) {

    const newQuote = prompt("Edit quote:", oldQuote)

    if(newQuote){

        fetch(API_URL + "/" + id, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                quote: newQuote
            })
        })
        .then(() => loadQuotes())

    }

}

function generateQuote() {

    fetch("/generate-quote")
    .then(response => response.json())
    .then(data => {

        document.getElementById("aiQuote").innerText = data.quote

    })

}

loadQuotes()