from app.listeners import messages, actions


def register_listeners(app):
    messages.register(app)
    actions.register(app)
