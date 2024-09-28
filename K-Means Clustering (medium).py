def k_means_clustering(points, k, initial_centroids, max_iterations):
    def distance(p1, p2):
        sm = 0.
        for i in range(len(p1)):
            sm += (p1[i] - p2[i])**2
        return sm**0.5
    def centroid(points):
        res = [0. for _ in range(len(points[0]))]
        for i in range(len(points[0])):
            res[i] = sum([p[i] for p in points]) / len(points)
        return res
    final_centroids = initial_centroids
    for i in range(max_iterations):
        min_dist = [float('inf') for _ in range(len(points))] #记录最小距离的中心点
        cluster = [-1 for _ in range(len(points))] #记录中心点的编号
        for idxpoint, point in enumerate(points):
            for idxcen, cen in enumerate(final_centroids):
                if distance(point, cen) < min_dist[idxpoint]:
                    cluster[idxpoint] = idxcen
                    min_dist[idxpoint] = distance(point, cen)
        new_centroids = [[] for _ in range(k)]
        for idxpoint, point in enumerate(points): #更新每个聚类的点集
            new_centroids[cluster[idxpoint]].append(point)
        # 更新每个聚类的中心点
        for idxcen, cen in enumerate(final_centroids):
            final_centroids[idxcen] = centroid(new_centroids[idxcen])
            
    return final_centroids

if __name__=="__main__":
    points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
    k = 2
    initial_centroids = [(1, 1), (10, 1)]
    max_iterations = 10
    print(k_means_clustering(points, k, initial_centroids, max_iterations))
    #output: [(1, 2), (10, 2)] 