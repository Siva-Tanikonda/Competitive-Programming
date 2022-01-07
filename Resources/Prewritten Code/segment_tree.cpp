/*
SEGMENT TREE
Purpose: This is a data structure that allows for quick range queries and point updates.
Time Complexity: [Build]O(n) [Update]O(lg(n)) [Query]O(lg(n))
Space Complexity: O(n)
*/

template<class T> struct segment_tree{
    vector<T> arr;
    int n;
    void init(int _n){
        n = _n;
        arr.resize(n * 4);
    }
    void init(vector<T> &lst){
        n = (int)lst.size();
        arr.resize(n * 4);
        build(1, 0, n - 1, lst);
    }
    void build(int vtx, int tl, int tr, vector<T> &lst){
        if(tl == tr) arr[vtx] = lst[tl];
        else{
            int mid = tl + (tr - tl) / 2;
            build(vtx * 2, tl, mid, lst);
            build(vtx * 2 + 1, mid + 1, tr, lst);
            arr[vtx] = arr[vtx * 2] + arr[vtx * 2 + 1];
        }
    }
    void update(int vtx, int tl, int tr, int pos, T val){
        if(tl == tr) arr[vtx] = val;
        else{
            int mid = tl + (tr - tl) / 2;
            if(pos <= mid) update(vtx * 2, tl, mid, pos, val);
            else update(vtx * 2 + 1, mid + 1, tr, pos, val);
            arr[vtx] = arr[vtx * 2] + arr[vtx * 2 + 1];
        }
    }
    void update(int pos, T val){
        update(1, 0, n - 1, pos, val);
    }
    T query(int vtx, int tl, int tr, int l, int r){
        if(l > r) return 0;
        else if(tl == l && tr == r) return arr[vtx];
        else{
            int mid = tl + (tr - tl) / 2;
            T p1 = query(vtx * 2, tl, mid, l, min(r, mid));
            T p2 = query(vtx * 2 + 1, mid + 1, tr, max(l, mid + 1), r);
            return p1 + p2;
        }
    }
    T query(int l, int r){
        return query(1, 0, n - 1, l, r);
    }
};