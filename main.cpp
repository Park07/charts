// ============================================================
// File: src/pattern.cpp
// Lines: 201-218
// Issue: Buffer overflow in create_plan_mgn() for patterns > 7 vertices
// ============================================================

void Pattern::create_plan_mgn(int max_vertices) {
    // BUG: Hardcoded array size assumes patterns <= 7 vertices
    int adj_matrix[8][8];  // Only supports up to 8 vertices!

    // When pattern has > 7 vertices, this causes out-of-bounds access
    for (int i = 0; i < vertex_count; i++) {
        for (int j = 0; j < vertex_count; j++) {
            adj_matrix[i][j] = get_edge(i, j);  // CRASH when i,j >= 8
        }
    }

}