def modal_template(title, blocks, callback_id=None, submit=None, close=None):
    dic = {
        "title": {
            "type": "plain_text",
            "text": title
        },
        "blocks": blocks,
        "type": "modal",
    }

    if submit != None:
        dic["submit"]={
            "type": "plain_text",
            "text": submit
        }
    if close != None: 
        dic["close"]={
            "type": "plain_text",
            "text": close
        }
    if (callback_id != None):
        dic["callback_id"]=callback_id

    return dic

# print(modal_template(
#     title="title",
#     blocks=[],
# ))