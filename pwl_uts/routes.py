def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('product', '/product')
    config.add_route('produk1', '/productCart')
    config.add_route('produk', '/product/{id}')
