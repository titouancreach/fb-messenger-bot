import requests


class FBMessagingEvent():
    """
    Parse facebook messaging event and add posibilities to respond to the sender
        :param rawevent The event sent by facebook webbhook.

    """

    def __init__(self, rawevent):
        if rawevent.get('message'):
            self.sender_id = rawevent['sender']['id']
            self.recipiend_id = rawevent['recipient']['id']
            self.msgtxt = rawevent['message']['text']


    def respond(self, msg):
        """
        Respond to the sender.
            :param msg Message to send back.
        """

        params = {
            'access_token': os.environ['PAGE_ACCESS_TOKEN']
        }
        headers = {
            'Content-Type': 'application/json'
        }

        data = json.dumps({
            'recipient': {
                'id': self.recipiend_id
            },
            'message': {
                'text': msg
            }
        })

        r = requests.post('https://graph.facebook.com/v2.6/me/messages', params=params, headers=headers, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)

