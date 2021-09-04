import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

if __name__ == "__main__":
    df = pd.read_csv("data/ca"
                     "r.data", header=None, engine="c")
    df = df.rename({
        0: "buying",
        1: "maint",
        2: "doors",
        3: "persons",
        4: "lug_boot",
        5: "safety",
        6: "class"
    }, axis=1)

    attributes = ["maint", "doors", "lug_boot", "safety", "class"]
    target = ["buying"]

    categories = [
        ["low", "med", "high", "vhigh"],  # buying category
        ["low", "med", "high", "vhigh"],  # maintenance category
        ["2", "3", "4", "5more"],  # doors category
        ["small", "med", "big"],  # lug_boot category
        ["low", "med", "high"],  # safety category
        ["unacc", "acc", "good", "vgood"],  # class category
    ]
    ordinal_encoder = OrdinalEncoder(categories=categories)
    print(ordinal_encoder)

    ordinal_encoder.fit(df[target + attributes])

    data = ordinal_encoder.transform(df[target + attributes])
    print(data)
