const gulp = require('gulp');
const browserSync = require('browser-sync');
const sass = require('gulp-sass');

gulp.task('sass', () => {
	return gulp
		.src(['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'])
		.pipe(
			sass({
				outputStyle: 'compressed',
			})
		)
		.pipe(gulp.dest('src/css'))
		.pipe(browserSync.stream());
});

gulp.task('js', () => {
	return gulp
		.src([
			'node_modules/bootstrap/dist/js/bootstrap.min.js',
			'node_modules/@popperjs/core/dist/umd/popper.min.js',
		])
		.pipe(gulp.dest('src/js'))
		.pipe(browserSync.stream());
});

gulp.task(
	'serve',
	gulp.series('sass', () => {
		browserSync.init({
			server: './src',
		});
		gulp.watch(
			['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'],
			gulp.series('sass')
		);
		gulp.watch('src/*.html').on('change', browserSync.reload);
	})
);

gulp.task('bootstrap-fonts', () => {
	return gulp
		.src('node_modules/bootstrap-icons/font/bootstrap-icons.css')
		.pipe(gulp.dest('src/css'));
});

gulp.task('fonts', () => {
	return gulp
		.src('node_modules/bootstrap-icons/font/fonts/*')
		.pipe(gulp.dest('src/fonts'));
});

gulp.task('default', gulp.series('js', 'bootstrap-fonts', 'fonts', 'serve'));
