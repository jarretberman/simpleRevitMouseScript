import pyautogui, sys


# x:220 y:100 enscape dropdown x:1340 y:1030
# 300,200
MODELS = int(input('Number of models: '))
VIEWS = int(input('Number of views per model: '))
TIME = int(input('Expected Render Time: '))
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)      


def views_loop (v): # +28y per view, move to 1000,70 for pano
    z = 0
    curr_y = 200

    while z < VIEWS:
        pyautogui.click(x=220,y=100)
        print('--views drop down open')
        pyautogui.click(x=300, y = curr_y)
        print('----view chosen', pyautogui.position())
        curr_y += 28
        pyautogui.click(x=1000,y=70)
        print('----render panoranma, wait 3 minutes')
        pyautogui.moveTo(220, 100, TIME)
        print('----pano finished')
        z += 1
    
    return print('--Views Loop Finished')


def models_loop(m):#1000 15 px movement    
    model_y = 1001
    w = 0
    while w < MODELS:
        pyautogui.click(x=1340,y=1030)
        print('model window open')
        pyautogui.click(x = 1340, y = model_y)
        print('--model chosen', pyautogui.position())
        model_y += 15
        views_loop(VIEWS)
        w += 1

    print('SCRIPT FINISHED')   


models_loop(MODELS)
# while count > 0:
#     x, y = pyautogui.position()
#     positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)      
    
#     print('Running Views Loop')
#     views_loop(VIEWS)
#     count -= 1