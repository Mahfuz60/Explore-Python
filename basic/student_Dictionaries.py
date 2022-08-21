studentId={
    "101":"Mahfuz Alam",
    "102":"Tonmoy Roy",
    "103":"Rafsan Faruk",
    "105":"Khairul Islam",
    "108":"Ahmed Hridoy",
    "107":"Rayhan Dollar",
    "110":"Kauser Badhon"
}

# Product List
product_Price={
    "apple":200,
    "mango":100,
    "new_product":{"Salt":2000,"Milk":150,"Cake":140},

}
# print(product_Price.get("new_product"))
# print(product_Price["mango"])
print(product_Price.get("apples","Not a valid Product"))