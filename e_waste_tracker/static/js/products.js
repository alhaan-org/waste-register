const editButtons = document.querySelectorAll("#edit-btn")
const form = document.querySelector("form")
const addBtn = document.getElementById("add")
const updateBtn = document.getElementById("update")
const deleteBtn = document.getElementById("delete")
const CSRF_TOKEN = document.querySelector("[name=csrfmiddlewaretoken]").value
const productName = document.getElementById("product-name")
const quantity = document.getElementById("quantity")
const type = document.getElementById("type")
const costPrice = document.getElementById("cost_price")
const soldPrice = document.getElementById("sold_price")
const description = document.getElementById("desc")
const isSold = document.getElementById("is_sold")

// editButtons.forEach((button) => {
//     button.addEventListener("click", async (event) => {
//         const id = event.target.closest("tr").dataset.id
//         console.log(id)
//     })
// })
const editProduct = (e) => {
    const rows = e.target.closest("tr")
    const desc = rows.dataset.description
    const cells = rows.querySelectorAll("td")
    const data = {
        name: cells[1].innerText,
        qty: cells[2].innerText,
        type: cells[7].innerText,
        costPrice: cells[5].innerText,
        soldPrice: cells[6].innerText,
        desc: desc,
    }

    productName.value = data.name
    quantity.value = data.qty
    type.value = data.type
    costPrice.value = data.costPrice
    soldPrice.value = data.soldPrice
    description.value = data.desc
}
const updateProduct = async (e) => {
    e.preventDefault()
}
const addProducts = async (e) => {
    e.preventDefault()
    const formData = new FormData(form)
    const data = Object.fromEntries(formData.entries())

    try {
        const response = await fetch("http://localhost:8000/app/api/add_item/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": CSRF_TOKEN
            },
            body: JSON.stringify(data)
        })
        const result = await response.json()
        console.log(result)
        form.reset()
        window.location.reload()
    }
    catch (error) {
        console.log(error)
    }
}

addBtn.addEventListener("click", addProducts)
editButtons.forEach(button => {
    button.addEventListener("click", editProduct)
})