from main import app


#  Регистрация category biznesa
@app.post('/register-business-category')
async def register_business_category_api(name: str):
    pass


# Registracia biznesa
@app.post('/register-business')
async def register_business_api(category_id: int, neme: str , card_number: int):
    pass


@app.get('/get-all-categories')
async def get_business_categories_api(exact_category: int = 0):
    pass


@app.get('/get-business')
async def get_exact_business_api(business_id: int, category_id: int):
    pass


@app.post('/pay-service')
async def pay_for_service(business_id: int, from_card: int, amount: float):
    pass


@app.delete('/delete-business')
async def delete_business_api(business_id: int):
    pass


@app.delete('/delete-business-category')
async def delete_business_category_api(category_id: int):
    pass


