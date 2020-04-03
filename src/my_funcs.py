import os


def submit(model, filename, comment=None):
    """
    
    """
    comment = comment if comment else filename[:-4]
    X_test = read_data("../data/test.csv")
    predictions = model.predict(X_test)
    submission = pd.DataFrame({"PassengerId": X_test.index, "Survived": predictions})
    submission.to_csv("/submissions/" + filename, index=False)
    print("Saved file: " + filename)
    cmd = f"kaggle competitions submit -c titanic -f {filename} -m {comment}"
    os.system(cmd)
    print("sumbission completed")
    return
