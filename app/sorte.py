import numpy as np
from flask import Blueprint, flash, render_template, redirect, request

bp = Blueprint("sorte", __name__)

drawn_numbers = []
arr_s = []
arr_o = []
arr_r = []
arr_t = []
arr_e = []

# sorteador de números
def prize_draw():
    while True:
        number = np.random.randint(1, 76)
        if not number in drawn_numbers:
            drawn_numbers.append(number)
            drawn_numbers.sort()
            break
    print("\n", drawn_numbers)
    print(len(drawn_numbers))
    return number

# interação com ui
@bp.route("/sorte", methods=('GET', 'POST'))
def sorte():
    num_luck = " "
    if request.method == 'POST':
        if len(drawn_numbers) >= 75:
            flash("Todos os números foram sorteados!")
        else:
            num_luck = prize_draw()
            if num_luck in range(1, 16):
                arr_s.append(num_luck)
                arr_s.sort()
                num_luck = "S"+str(num_luck)
            elif num_luck in range(16, 31):
                arr_o.append(num_luck)
                arr_o.sort()
                num_luck = "O"+str(num_luck)
            elif num_luck in range(31, 46):
                arr_r.append(num_luck)
                arr_r.sort()
                num_luck = "R"+str(num_luck)
            elif num_luck in range(46,61):
                arr_t.append(num_luck)
                arr_t.sort()
                num_luck = "T"+str(num_luck)
            elif num_luck in range(60, 76):
                arr_e.append(num_luck)
                arr_e.sort()
                num_luck = "E"+str(num_luck)
        
        
    return render_template("/bingo/sorte.html", num_luck= num_luck, arr_s=arr_s, arr_o=arr_o, arr_r=arr_r, arr_t=arr_t, arr_e=arr_e)

@bp.route("/reset")
def reset():
    drawn_numbers.clear()
    arr_s.clear()
    arr_o.clear()
    arr_r.clear()
    arr_t.clear()
    arr_e.clear()

    return redirect("/bingo")