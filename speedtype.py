import tkinter
from timeit import default_timer as timer
import random

def speed_test():
    speed_test_sentences = ['This is a random sentence to check speed.',
                 'I am lightning macqueen.']
    
    sentence = random.choice(speed_test_sentences)
    start = timer()
    main_window = tkinter.Tk()
    main_window.geometry('1000x400')

    label_1 = tkinter.Label(main_window, text=sentence, font='times 20')
    label_1.place(x=150, y=10)

    label_2 = tkinter.Label(main_window, text='Start typing', font='times 20')
    label_2.place(x=10, y=50)


    entry = tkinter.Entry(main_window)
    entry.place(width=500, height=100, x=280, y=55)

    def check_result():
        if entry.get() == sentence:
            end = timer()
            label_3.configure(text=f'Time:{round((end-start))}s')
        else:
            label_3.configure(text='Wrong input')

        label_3.option_clear()
    
    button_1 = tkinter.Button(main_window, text='Done', command=check_result, width='12', bg='grey')
    button_1.place(x=600, y=160)

    button_2 = tkinter.Button(main_window, text='Try Again', command=speed_test, width='12', bg='grey')
    button_2.place(x=700, y=160)

    label_3 = tkinter.Label(main_window, text='', font='times 20')
    label_3.place(x=10, y=200)

    
    main_window.mainloop()

if __name__ == '__main__':
    speed_test()


