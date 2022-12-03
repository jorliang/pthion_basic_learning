import  winsound
import win32com.client
import time
import speech
# speak_out = win32com.client.Dispatch('SAPI.SPVOICE')

# speak_out = win32com.client.Dispatch('Word.Application')

# def speak(str):
#     print(str)
#     speak_out.Speak(str)
#     winsound.PlaySound(str,winsound.SND_ASYNC)
#
#
# ak='簡単'
# time.sleep(1)
# speak(ak)

speech.say('でわ')