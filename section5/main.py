import pandas as pd
from sklearn.linear_model import LinearRegression
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

    attributes_categories = [
        ["low", "med", "high", "vhigh"],  # maintenance
        ["2", "3", "4", "5more"],  # number of doors
        ["small", "med", "big"],  # lug boot size
        ["low", "med", "high"],  # safety
        ["unacc", "acc", "good", "vgood"],  # class value
    ]

    target_category = [
        ["low", "med", "high", "vhigh"]  # buying
    ]

    attributes_encoder = OrdinalEncoder(categories=attributes_categories)
    attributes_encoder.fit(df[attributes])
    x = attributes_encoder.transform(df[attributes])

    target_encoder = OrdinalEncoder(categories=target_category)
    target_encoder.fit(df[target])
    y = target_encoder.transform(df[target])

    regression = LinearRegression()
    regression.fit(x, y)

    prediction_attributes = [[
        "high",  # maintenance
        "4",  # number of doors
        "big",  # lug boot size
        "high",  # safety
        "good"  # class value
    ]]

    encoded_attributes = attributes_encoder.transform(prediction_attributes)
    print(encoded_attributes)
    
    print(attributes_encoder.inverse_transform(encoded_attributes))
    
    prediction = regression.predict(encoded_attributes)
    print(prediction)

    decoded_prediction = target_encoder.inverse_transform(prediction)
    print(decoded_prediction)
