#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec2 in_texcoord_0;
out vec2 uv0;

void main() {
    gl_Position = vec4(in_position, 1);
    uv0 = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

out float fragColor;
in vec2 uv0;

uniform sampler2D texture;

const ivec2 kpos[9] = ivec2[9](
    ivec2(-1,  1),  ivec2(0,  1),  ivec2(1,  1),
    ivec2(-1,  0),  ivec2(0,  0),  ivec2(1,  0),
    ivec2(-1, -1),  ivec2(0, -1),  ivec2(1, -1)
);

const float external_flow = .4;

const float poi_kernel[9] = float[9](
      0.0, .25,  0.0,
     .25,   0,  .25,
      0.0, .25,  0.0
);

float poisson(ivec2 uv, sampler2D source) {
    float value = 0;
    for (int i = 0; i < 9; i++) {
        value += texelFetch(source, uv + kpos[i], 0).r * poi_kernel[i];
    }
    return value;
}

void main() {
    ivec2 uv = ivec2(gl_FragCoord.xy);
    fragColor = poisson(uv, texture) * 0.5;
}
#endif
