from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

# Parameters
BATCH_SIZE = 200
GAMMA = -20.0
PLOT = True

# Generate dataset: moons or circles
X, y = datasets.make_moons(n_samples=50, noise=0.1)
# X, y = datasets.make_circles(n_samples=100, factor=0.5, noise=0.1)

# Convert labels: 1 for class 1, -1 for class 0
y = np.array([1 if label == 1 else -1 for label in y], dtype=np.float32)

# Select random test batch
random_indices = np.random.choice(len(X), size=BATCH_SIZE)
X_test = X[random_indices]
y_test = y[random_indices].reshape(-1, 1)


def rbf_kernel_prediction(X_train, y_train, X_predict, gamma_val):
    """
    Predict labels using RBF kernel SVM decision function.

    Args:
        X_train (np.array): Training points (NxD).
        y_train (np.array): Training labels (Nx1).
        X_predict (np.array): Points to classify (MxD).
        gamma_val (float): Kernel gamma parameter.

    Returns:
        np.array: Predicted labels (1 or -1) shape (Mx1).
    """
    # Compute squared norms
    sum_sq_train = np.sum(X_train ** 2, axis=1).reshape(-1, 1)  # (N,1)
    sum_sq_predict = np.sum(X_predict ** 2, axis=1).reshape(1, -1)  # (1,M)

    # Compute kernel matrix using broadcasting and dot products
    K = sum_sq_train - 2 * np.dot(X_train, X_predict.T) + sum_sq_predict
    K *= gamma_val
    K = np.exp(K)  # RBF kernel

    # Compute decision values
    decision_values = np.dot(y_train.T, K)
    return np.sign(decision_values).flatten()


# Prediction on test set
predictions = rbf_kernel_prediction(X_test, y_test, X_test, GAMMA)

# Calculate accuracy
correct = predictions == y_test.flatten()
accuracy = np.mean(correct)
print(f"\nClassification accuracy on test set: {accuracy * 100:.2f}%")


if PLOT:
    # Prepare plotting data
    data_with_labels = np.c_[X, y]
    x_pos = data_with_labels[data_with_labels[:, 2] == 1][:, 0]
    y_pos = data_with_labels[data_with_labels[:, 2] == 1][:, 1]
    x_neg = data_with_labels[data_with_labels[:, 2] == -1][:, 0]
    y_neg = data_with_labels[data_with_labels[:, 2] == -1][:, 1]

    # Define meshgrid for decision boundary
    x_min, y_min = np.amin(X, axis=0) - 1
    x_max, y_max = np.amax(X, axis=0) + 1

    grid_points = 30
    xx = np.linspace(x_min, x_max, grid_points)
    yy = np.linspace(y_min, y_max, grid_points)
    xs, ys = np.meshgrid(xx, yy)
    grid = np.c_[xs.ravel(), ys.ravel()]

    # Predict on grid
    Z = rbf_kernel_prediction(X, y.reshape(-1, 1), grid, GAMMA)
    Z = Z.reshape(xs.shape)

    # Plot results
    fig = plt.figure(figsize=(12, 5))
    fig.suptitle('Support Vector Machine with RBF Kernel')

    # 2D decision boundary and points
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.scatter(x_pos, y_pos, c='green', marker='o', label='Class +1')
    ax1.scatter(x_neg, y_neg, c='red', marker='x', label='Class -1')
    ax1.contourf(xx, yy, Z, cmap=ListedColormap(['#ad301d', 'g']), alpha=0.3)
    ax1.grid(True)
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.legend()

    # 3D scatter plot
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.scatter(X[:, 0], X[:, 1], y, c=y, cmap=ListedColormap(['red', 'green']), s=50)
    ax2.set_xlabel('X axis')
    ax2.set_ylabel('Y axis')
    ax2.set_zlabel('Class')

    plt.show()