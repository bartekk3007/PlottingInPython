from PIL import Image
import matplotlib.pyplot as plt

# Utwórz obraz 2x2 w trybie RGB
image = Image.new("RGB", (2, 2))

# Dane pikseli w formacie (R, G, B)
data = [
    (255, 0, 0),   # Czerwony
    (0, 255, 0),   # Zielony
    (0, 0, 255),   # Niebieski
    (255, 255, 0)  # Żółty
]

# Ustaw dane w obrazie
image.putdata(data)

# Zapisz wynik
image.save("output.png")

# plt.figure()

plt.imshow(image)
plt.axis("on")
plt.show()

plt.imshow(image)
plt.axis(False)
plt.show()

plt.imshow(image)
plt.grid("on")
plt.show()

plt.imshow(image)
plt.grid(False)
plt.show()
