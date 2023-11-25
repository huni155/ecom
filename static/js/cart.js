var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        var productId = this.dataset.product;
        var productPrice = this.dataset.price;
        var action = this.dataset.action;
        var productName = this.dataset.name;
        var productImg = this.dataset.img;
        // console.log('productId:', productId, 'Action:', action)

        // console.log('USER:', user)
        // addCookieItem(productId, productPrice, action, productName, productImg)
        if (user === 'AnonymousUser') {
            addCookieItem(productId, action);
        }
        else {
            updateUserOrder(productId, action)
        }
        console.log("ID:", productId);
    });
}

// function addCookieItem(productId, productPrice, action, productName, productImg) {
//     // console.log('not authenticated')
//     console.log(productPrice);
//     let isExists = false;
//     cart.forEach(item => {
//         if(productId == item.productId) {
//             isExists = true;
//         }
//     });
//     if (action == 'add') {
//         if (isExists) {
//             cart.forEach(item => {
//                 if(productId == item.productId) {
//                     item.quantity +=1
//                 }
//             });
//         }
//         else {
//             cart.push({ productId: productId, quantity: 1 , price: productPrice, name: productName, imageURL: productImg});
//         }
//         const alert = document.querySelector('.alert');
//         alert.innerHTML = "successfully to add new item";
//         alert.style.display = "block!important"
//     }

//     if (action == 'remove') {
//         if (isExists) {
//             cart.forEach(item => {
//                 if(productId == item.productId) {
//                     delete item
//                     console.log(cart)
//                 }
//             });
//         }
//         cart[productId][quantity] -= 1

//         if (cart[productId][quantity] <= 0) {
//             console.log('remove item')
//             delete cart[productId]
//         }
//     }

//     var totalCartItems = 0

//     cart.forEach(item => {
//         totalCartItems += item.quantity
//     });

//     console.log('cart:', cart)
//     console.log('total:', totalCartItems)

//     document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'

// }

function addCookieItem(productId, action) {
    console.log("product id: ", productId);
    console.log("not logged in");
    console.log('csrf: ', csrftoken);
    if (action == "add") {
        if (cart[productId] == undefined) {
            cart[productId] = { quantity: 1 };
        } else {
            cart[productId]["quantity"] += 1;
        }
    }

    if (action == "remove") {
        cart[productId]["quantity"] -= 1;
        if (cart[productId]["quantity"] <= 0) {
            console.log("remove item");
            delete cart[productId];
        }
    }
    console.log("cart:", cart);
    console.log("string: ", JSON.stringify(cart));
    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
    location.reload()
}

function updateUserOrder(productId, action) {
    console.log("User is authenticated, sending data");

    var url = "/update_item/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ productId: productId, action: action }),
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            location.reload();
        });
}