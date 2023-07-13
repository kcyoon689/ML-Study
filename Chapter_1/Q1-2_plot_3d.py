# Plot the following training set in three-dimensional space and whether it is linearly separable and why.
# 다음 훈련 집합을 3차원 공간에 플롯하고 선형 분리 가능한지 여부와 그 이유를 설명합니다.

import plotly.graph_objects as go

# below is 1
x1 = [0, 0, 1]
y1 = [0, 1, 1]
z1 = [0, 1, 1]

# below  is -1
x2 = [1, 0, 0]
y2 = [0, 0, 1]
z2 = [1, 1, 0]

fig = go.Figure()

# fig = go.Figure(data=[go.Scatter3d(x=x1, y=y1, z=z1, mode='markers')])
# fig = go.Figure(data=[go.Scatter3d(x=x2, y=y2, z=z2, mode='markers')])
fig.add_trace(go.Scatter3d(x=x1, y=y1, z=z1, mode='markers'))
fig.add_trace(go.Scatter3d(x=x2, y=y2, z=z2, mode='markers'))

fig.show()