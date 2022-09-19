from app.listeners import messages, events, actions, commands


def register_listeners(app):
    messages.register(app)
    events.register(app)
    actions.register(app)
    commands.register(app)
