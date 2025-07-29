# ---/// 2D Vector Plotter Step-by-Step Explainer ///---

import matplotlib.pyplot as plt

print("Let's plot a 2D vector and see its geometric representation!\n")
vec = [float(x) for x in input("Enter your 2D vector (x,y): ").split(",")]

if len(vec) != 2:
    print("You must enter exactly 2 values for a 2D vector.")
else:
    print("\nWe'll draw this vector from the origin (0,0) to the point ({},{}).".format(vec[0], vec[1]))
    print("This helps visualize direction and magnitude in the x-y plane.")

    # Plot
    plt.figure(figsize=(6,6))
    plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color='b')
    plt.xlim(-abs(vec[0])-2, abs(vec[0])+2)
    plt.ylim(-abs(vec[1])-2, abs(vec[1])+2)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Vector Plot')
    plt.text(vec[0], vec[1], f"({vec[0]}, {vec[1]})", fontsize=12, color='r')
    plt.show()
