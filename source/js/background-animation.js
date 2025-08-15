const device_width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

if (device_width > 600) {
    new CanvasNice({
        point_dist: 100,
        point_count: 60,
        point_size: {
            min: 1,
            max: 2
        },
        point_slow_down_rate: 0.8,
        point_color: '238,232,190',
        line_color: '212,195,55',
        line_width_multiplier: 1.5,
        max_point_speed: 0.5,
        zIndex: -1,
        canvas_opacity: 1,
        render_rate: 30,
        chunk_capacity: 15,
        chunk_size_constant: 1,
        pointer_inter_type: -1
    });
}
